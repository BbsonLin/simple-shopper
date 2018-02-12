import Vue from 'vue'
import Router from 'vue-router'
import Shop from '@/components/Shop'
import Cart from '@/components/Cart'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Shop',
      component: Shop
    },
    {
      path: '/cart',
      name: 'Cart',
      component: Cart
    }
  ]
})
