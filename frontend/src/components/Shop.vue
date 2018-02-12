<template>
<div class="shop">
  <shopper-header></shopper-header>
  <shopper-jumbotron></shopper-jumbotron>
  <shopper-product></shopper-product>
</div>
</template>

<script>
import ShopperHeader from './Header'
import ShopperJumbotron from './Jumbotron'
import ShopperProduct from './Product/Product'
export default {
  name: 'cart',
  components: {
    ShopperHeader,
    ShopperJumbotron,
    ShopperProduct
  }
}
</script>

<style lang="scss">
</style>
