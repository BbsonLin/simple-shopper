// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import Moment from 'moment'
import MomentTimezone from 'moment-timezone'
import VueMultiselect from 'vue-multiselect'
import 'vue-multiselect/dist/vue-multiselect.min.css'

Vue.component('multiselect', VueMultiselect)

window.moment = Moment
window.tz = MomentTimezone

// moment filter setting
Vue.filter('moment', function (timestamp) {
  var timezone = window.moment.tz.guess()
  return window.moment.unix(timestamp).tz(timezone).format('YYYY-MM-DD HH:mm')
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
