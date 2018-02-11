<template>
<div class="cart">
  <h1 class="cart-title">Cart</h1>
  {{ totalNumber }}
  <empty v-if="!totalNumber"></empty>
  <!-- <stepone v&#45;if="step===1"></stepone> -->
  <button class="btn btn-primary check-button" v-if="totalNumber">下一步</button>
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

.check-button {
  margin-left: auto;
}
</style>
