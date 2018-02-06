<template>
  <div id="app">
    <shopper-header></shopper-header>
    <shopper-jumbotron></shopper-jumbotron>
    <shopper-product></shopper-product>
    <shopper-footer></shopper-footer>
    <!-- <router-view/> -->
  </div>
</template>

<script>
import ShopperHeader from './components/Header'
import ShopperJumbotron from './components/Jumbotron'
import ShopperProduct from './components/Product/Product'
import ShopperFooter from './components/Footer'

export default {
  name: 'app',
  components: {
    ShopperHeader,
    ShopperJumbotron,
    ShopperProduct,
    ShopperFooter
  }
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
