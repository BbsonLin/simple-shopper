<template>
  <div id="app">
    <shopper-header></shopper-header>
    <shopper-jumbotron></shopper-jumbotron>
    <router-view/>
    <shopper-footer></shopper-footer>
  </div>
</template>

<script>

import ShopperHeader from './Components/Header'
import ShopperJumbotron from './Components/Jumbotron'
import ShopperFooter from './Components/Footer'
export default {
  name: 'app',
  components: {
    ShopperHeader,
    ShopperJumbotron,
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
