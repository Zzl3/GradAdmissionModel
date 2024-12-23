from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import pymysql
from dbutils.pooled_db import PooledDB
import random
from datetime import datetime, timedelta
import hashlib

# 数据库连接池
pool = PooledDB(
    creator=pymysql,
    maxconnections=6,
    mincached=2,
    maxcached=5,
    host='127.0.0.1',
    user='root',
    password='@zzl030318',
    database='front',
    charset='utf8mb4'
)

app = Flask(__name__)

# 简化 CORS 配置
CORS(app, 
     resources={r"/*": {"origins": "*"}},
     supports_credentials=False,
     methods=["GET", "POST", "OPTIONS"])

# 添加错误处理
@app.errorhandler(Exception)
def handle_error(error):
    print(f"Error occurred: {str(error)}")  # 添加服务器端日志
    return jsonify({
        'success': False,
        'message': str(error)
    }), getattr(error, 'code', 500)

# 根路由
@app.route('/')
def index():
    try:
        return jsonify({
            'success': True,
            'message': 'Welcome to the API'
        })
    except Exception as e:
        print(f"Error in index route: {str(e)}")
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500
    
# 测试路由
@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({
        'success': True,
        'message': 'Backend is working!'
    })

# 生成验证码
def generate_verification_code():
    return ''.join(random.choices('0123456789', k=6))

# 发送验证码（这里模拟发送，实际项目中需要集成短信服务）
def send_sms(phone, code):
    print(f"向{phone}发送验证码: {code}")
    return True

@app.route('/api/send-code', methods=['POST'])
def send_verification_code():
    try:
        data = request.get_json()
        phone = data.get('phone')
        code_type = data.get('type', 'login')  # 默认为登录验证码
        
        if not phone:
            return jsonify({
                'success': False,
                'message': '手机号不能为空'
            })
        
        with pool.connection() as conn, conn.cursor() as cursor:
            # 如果是找回密码，检查用户是否存在
            if code_type == 'forget':
                cursor.execute("SELECT id FROM users WHERE phone = %s", (phone,))
                if not cursor.fetchone():
                    return jsonify({
                        'success': False,
                        'message': '该手机号未注册'
                    })
            
            # 如果是注册，检查用户是否已存在
            if code_type == 'register':
                cursor.execute("SELECT id FROM users WHERE phone = %s", (phone,))
                if cursor.fetchone():
                    return jsonify({
                        'success': False,
                        'message': '该手机号已注册'
                    })
            
            # 检查是否有未过期的验证码
            cursor.execute("""
                SELECT code, expired_at 
                FROM verification_codes 
                WHERE phone = %s AND expired_at > NOW() AND is_used = 0
                AND type = %s
                ORDER BY created_at DESC LIMIT 1
            """, (phone, code_type))
            
            existing_code = cursor.fetchone()
            if existing_code:
                print(f"Existing {code_type} code for {phone}: {existing_code[0]}")
                return jsonify({
                    'success': True,
                    'message': '验证码发送成功'
                })
            
            # 生成新验证码
            code = generate_verification_code()
            expired_at = datetime.now() + timedelta(minutes=5)
            
            # 存储验证码
            cursor.execute("""
                INSERT INTO verification_codes (phone, code, expired_at, type)
                VALUES (%s, %s, %s, %s)
            """, (phone, code, expired_at, code_type))
            
            conn.commit()
            print(f"Generated new {code_type} code for {phone}: {code}")
            
            return jsonify({
                'success': True,
                'message': '验证码发送成功'
            })
            
    except Exception as e:
        print(f"Error in send_verification_code: {str(e)}")
        return jsonify({
            'success': False,
            'message': f'发送验证码失败: {str(e)}'
        }), 500

@app.route('/api/phone-login', methods=['POST'])
def phone_login():
    try:
        data = request.get_json()
        phone = data.get('phone')
        code = data.get('code')
        
        print(f"Phone login attempt - Phone: {phone}, Code: {code}")  # 调试日志
        
        if not all([phone, code]):
            return jsonify({
                'success': False,
                'message': '请填写手机号和验证码'
            })
        
        with pool.connection() as conn, conn.cursor() as cursor:
            # 验证验证码
            cursor.execute("""
                SELECT id 
                FROM verification_codes 
                WHERE phone = %s AND code = %s AND expired_at > NOW() AND is_used = 0
                ORDER BY created_at DESC LIMIT 1
            """, (phone, code))
            
            code_record = cursor.fetchone()
            if not code_record:
                return jsonify({
                    'success': False,
                    'message': '验证码无效或已过期'
                })
            
            # 标记验证码为已使用
            cursor.execute("""
                UPDATE verification_codes 
                SET is_used = 1 
                WHERE id = %s
            """, (code_record[0],))
            
            # 检查用户是否存在
            cursor.execute("""
                SELECT id, phone 
                FROM users 
                WHERE phone = %s
            """, (phone,))
            
            user = cursor.fetchone()
            if not user:
                # 创建新用户
                cursor.execute("""
                    INSERT INTO users (phone) 
                    VALUES (%s)
                """, (phone,))
                user_id = cursor.lastrowid
            else:
                user_id = user[0]
            
            conn.commit()
            
            print(f"Successful phone login for user: {phone}")  # 调试日志
            
            return jsonify({
                'success': True,
                'message': '登录成功',
                'data': {
                    'user_id': user_id,
                    'phone': phone
                }
            })
            
    except Exception as e:
        print(f"Phone login error: {str(e)}")  # 错误日志
        return jsonify({
            'success': False,
            'message': f'登录失败: {str(e)}'
        }), 500

@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        phone = data.get('phone')
        code = data.get('code')
        password = data.get('password')
        
        print(f"Registering user - Phone: {phone}, Code: {code}")  # 调试日志
        
        if not all([phone, code, password]):
            return jsonify({
                'success': False,
                'message': '请填写所有必填项'
            })
        
        with pool.connection() as conn, conn.cursor() as cursor:
            # 验证验证码
            cursor.execute("""
                SELECT id, code, expired_at 
                FROM verification_codes 
                WHERE phone = %s AND expired_at > NOW() AND is_used = 0
                ORDER BY created_at DESC LIMIT 1
            """, (phone,))
            
            code_record = cursor.fetchone()
            print(f"Found code record: {code_record}")  # 调试日志
            
            if not code_record:
                return jsonify({
                    'success': False,
                    'message': '未找到有效的验证码'
                })
                
            if code_record[1] != code:
                return jsonify({
                    'success': False,
                    'message': '验证码错误'
                })
            
            # 检查手机号是否已注册
            cursor.execute("SELECT id FROM users WHERE phone = %s", (phone,))
            if cursor.fetchone():
                return jsonify({
                    'success': False,
                    'message': '该手机号已注册'
                })
            
            # 密码加密
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            
            # 创建新用户
            cursor.execute("""
                INSERT INTO users (phone, password) 
                VALUES (%s, %s)
            """, (phone, hashed_password))
            
            # 标记验证码为已使用
            cursor.execute("""
                UPDATE verification_codes 
                SET is_used = 1 
                WHERE id = %s
            """, (code_record[0],))
            
            conn.commit()
            print(f"Successfully registered user with phone: {phone}")  # 调试日志
            
            return jsonify({
                'success': True,
                'message': '注册成功'
            })
            
    except Exception as e:
        print(f"Error in register: {str(e)}")
        return jsonify({
            'success': False,
            'message': f'注册失败: {str(e)}'
        }), 500

@app.route('/api/account-login', methods=['POST'])
def account_login():
    try:
        data = request.get_json()
        phone = data.get('phone')
        password = data.get('password')
        
        print(f"Account login attempt - Phone: {phone}")  # 调试日志
        
        if not all([phone, password]):
            return jsonify({
                'success': False,
                'message': '请填写手机号和密码'
            })
        
        with pool.connection() as conn, conn.cursor() as cursor:
            # 查找用户
            cursor.execute("""
                SELECT id, phone, password 
                FROM users 
                WHERE phone = %s
            """, (phone,))
            
            user = cursor.fetchone()
            if not user:
                return jsonify({
                    'success': False,
                    'message': '用户不存在'
                })
            
            # 验证密码
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if hashed_password != user[2]:
                return jsonify({
                    'success': False,
                    'message': '密码错误'
                })
            
            # 记录登录
            cursor.execute("""
                INSERT INTO login_history (user_id, login_type, ip_address)
                VALUES (%s, 'account', %s)
            """, (user[0], request.remote_addr))
            
            conn.commit()
            
            print(f"Successful login for user: {phone}")  # 调试日志
            
            return jsonify({
                'success': True,
                'message': '登录成功',
                'data': {
                    'user_id': user[0],
                    'phone': user[1]
                }
            })
            
    except Exception as e:
        print(f"Account login error: {str(e)}")  # 错误日志
        return jsonify({
            'success': False,
            'message': f'登录失败: {str(e)}'
        }), 500

# 重置密码
@app.route('/api/reset-password', methods=['POST'])
def reset_password():
    try:
        data = request.get_json()
        phone = data.get('phone')
        code = data.get('code')
        new_password = data.get('newPassword')
        
        if not all([phone, code, new_password]):
            return jsonify({
                'success': False,
                'message': '请填写所有必填项'
            })
        
        with pool.connection() as conn, conn.cursor() as cursor:
            # 验证验证码
            cursor.execute("""
                SELECT id 
                FROM verification_codes 
                WHERE phone = %s AND code = %s AND expired_at > NOW() 
                AND is_used = 0 AND type = 'forget'
                ORDER BY created_at DESC LIMIT 1
            """, (phone, code))
            
            code_record = cursor.fetchone()
            if not code_record:
                return jsonify({
                    'success': False,
                    'message': '验证码无效或已过期'
                })
            
            # 更新密码
            hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
            cursor.execute("""
                UPDATE users 
                SET password = %s 
                WHERE phone = %s
            """, (hashed_password, phone))
            
            # 标记验证码为已使用
            cursor.execute("""
                UPDATE verification_codes 
                SET is_used = 1 
                WHERE id = %s
            """, (code_record[0],))
            
            conn.commit()
            
            return jsonify({
                'success': True,
                'message': '密码重置成功'
            })
            
    except Exception as e:
        print(f"Error in reset_password: {str(e)}")
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
