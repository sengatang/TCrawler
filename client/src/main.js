// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import App from './App'
import router from './router'
import VueTimepicker from 'vue2-timepicker'
import ElementUI from 'element-ui'
import VueResource from 'vue-resource'
import 'element-ui/lib/theme-chalk/index.css'
import './config'

Vue.use(BootstrapVue)
Vue.use(VueTimepicker)
Vue.use(ElementUI)
Vue.use(VueResource)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: {
    App,
    VueTimepicker
  }
})

Vue.http.options.emulateJSON = true
Vue.http.options.crossOrigin = true
Vue.http.options.emulateHTTP = true
Vue.http.interceptors.push((request, next) => {
  // Vue.http.headers.common['Authorization'] = 'token ' + window.localStorage.token
  request.credentials = true
  console.log('here')
  request.headers.set('Authorization', 'token ' + window.localStorage.token)
  Vue.http.headers.common['Authorization'] = 'token ' + window.localStorage.token
  console.log(request.headers)
  next()
})
