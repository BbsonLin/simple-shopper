<template>
<div class="cart">
  <h1 class="cart-title">Cart</h1>
  <empty v-if="!totalNumber"></empty>
</div>
</template>

<script>
import Empty from './Empty'
import { mapGetters } from 'vuex'
export default {
  name: 'cart',
  components: {
    Empty
  },
  computed: {
    ...mapGetters({
      totalNumber: 'getTotalNumber'
    })
  }
}
</script>

<style lang="scss">
.cart {
  padding: 10px;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
