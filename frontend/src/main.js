import Vue from 'vue/dist/vue.js'
import VueRouter from 'vue-router'
import App from './App'
import router from './router'
import VueClip from 'vue-clip'

Vue.use(VueRouter)
Vue.use(VueClip)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
