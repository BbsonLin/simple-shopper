import Vue from 'vue'
import Router from 'vue-router'
import Product from '@/components/Product/Product'
import Cart from '@/components/Cart'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Shop',
      component: Product
    },
    {
      path: '/cart',
      name: 'Cart',
      component: Cart
    }
  ]
})
