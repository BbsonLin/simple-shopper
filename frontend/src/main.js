// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import VueMultiselect from 'vue-multiselect'
import 'vue-multiselect/dist/vue-multiselect.min.css'

Vue.component('multiselect', VueMultiselect)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
