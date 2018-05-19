<template>
  <div class="app flex-row align-items-center">
    <div class="container">
      <b-row class="justify-content-center">
        <b-col md="6" sm="8">
          <b-card no-body class="mx-4">
            <b-card-body class="p-4">
              <h1>Register</h1>
              <p class="text-muted">注册TCrawler</p>
              <el-form ref="register" status-icon :model="register" :rules="registerRule">
                <el-form-item prop="username">
                  <el-input
                    placeholder="请输入用户名"
                    v-model="register.username">
                    <i slot="prefix" class="el-input__icon icon-user"></i>
                  </el-input> 
                </el-form-item> 
                <el-form-item prop="email">
                  <el-input
                    placeholder="请输入邮箱"
                    v-model="register.email">
                    <i slot="prefix" class="el-input__icon icon-envelope"></i>
                  </el-input> 
                </el-form-item>
                <el-form-item prop="password">
                  <el-input
                    placeholder="请输入密码"
                    v-model="register.password"
                    type="password">
                    <i slot="prefix" class="el-input__icon icon-lock"></i>
                  </el-input> 
                </el-form-item>
                <el-form-item prop="password2">
                  <el-input
                    placeholder="请确认密码"
                    v-model="register.password2" 
                    type="password">
                    <i slot="prefix" class="el-input__icon icon-lock"></i>
                  </el-input> 
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" @click="submitForm('register')">确认注册</el-button>
                </el-form-item>
              </el-form>
            </b-card-body>
          </b-card>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data () {
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.register.password !== '') {
          this.$refs.register.validateField('password2')
        }
        callback()
      }
    }
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.register.password2) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      register: {
        username: '',
        email: '',
        password: '',
        password2: ''
      },
      registerRule: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' }
        ],
        email: [
          { required: true, message: '请输入邮箱地址', trigger: 'blur' },
          { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
        ],
        password: [
          { validator: validatePass, trigger: 'blur' }
        ],
        password2: [
          { validator: validatePass2, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$http.post('http://localhost:8000/register/', {
            username: this.register.username,
            email: this.register.email,
            password: this.register.password,
            ins: ''
          }).then(response => {
            this.$notify({
              title: '注册成功',
              message: '您已成功注册TClawer，请登陆',
              type: 'success'
            })
            this.$router.push({path: '/pages/login'})
          }, response => {})
        } else {
          console.log('error submit!!')
          return false
        }
      })
    }
  }
}
</script>