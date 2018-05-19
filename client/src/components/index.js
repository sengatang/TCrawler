import Aside from './Aside.vue'
import Breadcrumb from './Breadcrumb.vue'
import Callout from './Callout.vue'
import Footer from './Footer.vue'
import Header from './Header/Header.vue'
import Sidebar from './Sidebar/Sidebar.vue'
import Switch from './Switch.vue'
import Vue from 'vue'
import Router from 'vue-router'
import VueResource from 'vue-resource'
Vue.use(Router)
Vue.use(VueResource)

export {
  Aside,
  Breadcrumb,
  Callout,
  Footer,
  Header,
  Sidebar,
  Switch
}

if (!window.localStorage.token) {
  this.$notify({
    title: '请登陆',
    message: '请登陆后方可使用',
    type: 'warning'
  })
  this.$router.push({path: '/pages/login'})
} else {
  Vue.http.headers.common['Authorization'] = 'token ' + window.localStorage.token
}
