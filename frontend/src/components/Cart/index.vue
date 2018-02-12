<template>
<div class="cart">
  <h1 class="cart-title">Cart</h1>
  <empty v-if="!totalNumber"></empty>
  <stepone v-if="totalNumber && step===1"></stepone>
  <steptwo v-if="totalNumber && step===2"></steptwo>
</div>
</template>

<script>
import Empty from './Empty'
import Stepone from './Stepone'
import Steptwo from './Steptwo'
import { mapGetters } from 'vuex'
export default {
  name: 'cart',
  components: {
    Empty,
    Stepone,
    Steptwo
  },
  computed: {
    ...mapGetters({
      totalNumber: 'getTotalNumber',
      step: 'getStep'
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
  width: 80%;
  display: flex;
  justify-content: flex-end;
}
</style>
