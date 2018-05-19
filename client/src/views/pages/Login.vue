<template>
  <div class="app flex-row align-items-center">
    <div class="container">
      <b-row class="justify-content-center">
        <b-col md="8">
          <b-card-group>
            <b-card no-body class="p-4">
              <b-card-body>
                <h1>Login</h1>
                <p class="text-muted">Sign In to your account</p>
                <b-input-group class="mb-3">
                  <b-input-group-prepend><b-input-group-text><i class="icon-user"></i></b-input-group-text></b-input-group-prepend>
                  <input type="text" class="form-control" v-model="username" placeholder="Username">
                </b-input-group>
                <b-input-group class="mb-4">
                  <b-input-group-prepend><b-input-group-text><i class="icon-lock"></i></b-input-group-text></b-input-group-prepend>
                  <input type="password" class="form-control" v-model="password" placeholder="Password">
                </b-input-group>
                <b-row>
                  <b-col cols="6">
                    <b-button variant="primary" class="px-4" @click="validiateLogin">Login</b-button>
                  </b-col>
                  <b-col cols="6" class="text-right">
                    <b-button variant="link" class="px-0">Forgot password?</b-button>
                  </b-col>
                </b-row>
              </b-card-body>
            </b-card>
            <b-card no-body class="text-white bg-primary py-5 d-md-down-none" style="width:44%">
              <b-card-body class="text-center">
                <div>
                  <h2>Sign up</h2>
                  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                  <b-button variant="primary" class="active mt-3" @click="goRegister">Register Now!</b-button> 
                  <!-- https://www.cnblogs.com/wisewrong/p/6277262.html -->
                </div>
              </b-card-body>
            </b-card>
          </b-card-group>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  name: 'Login',
  methods: {
    goRegister: function () {
      this.$router.push({path: '/pages/register'})
    },
    validiateLogin: function () {
      this.$http.post('http://localhost:8000/login/', {
        username: this.username,
        password: this.password
      }).then(response => {
        this.$router.push({path: '/dashboard'})
        window.localStorage.setItem('token', response.data['token'])
        window.localStorage.setItem('username', this.username)
        // let token = response.body
      }, response => {})
    }
  }
}
</script>
