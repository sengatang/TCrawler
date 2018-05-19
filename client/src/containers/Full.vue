<template>
  <div class="app">
    <AppHeader/>
    <div class="app-body">
      <Sidebar :navItems="nav"/>
      <main class="main">
        <breadcrumb :list="list"/>
        <div class="container-fluid">
          <router-view></router-view>
        </div>
      </main>
      <AppAside/>
    </div>
    <AppFooter/>
  </div>
</template>

<script>
import Vue from 'vue'
import nav from '../_nav'
import { Header as AppHeader, Sidebar, Aside as AppAside, Footer as AppFooter, Breadcrumb } from '../components/'

export default {
  name: 'full',
  components: {
    AppHeader,
    Sidebar,
    AppAside,
    AppFooter,
    Breadcrumb
  },
  data () {
    return {
      nav: nav.items
    }
  },
  computed: {
    name () {
      return this.$route.name
    },
    list () {
      return this.$route.matched
    }
  },
  mounted () {
    if (!window.localStorage.token) {
      this.$notify({
        title: '请登陆',
        message: '请登陆后方可使用',
        type: 'warning'
      })
      this.$router.push({path: '/pages/login'})
    } else {
      Vue.http.options.emulateJSON = true
      Vue.http.options.crossOrigin = true
      Vue.http.options.emulateHTTP = true
      console.log('alright')
      Vue.http.headers.common['Authorization'] = 'token ' + window.localStorage.token
    }
  }
}
</script>
