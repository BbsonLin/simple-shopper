<template>
  <div id="app">
    <router-view/>
    <shopper-footer></shopper-footer>
  </div>
</template>

<script>
import ShopperFooter from './components/Footer'
export default {
  name: 'app',
  components: {
    ShopperFooter
  }
}
</script>

<style lang="scss">
html,
body {
  height: 100%;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  display: flex;
  flex-direction: column;
}
</style>
