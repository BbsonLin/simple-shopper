<template>
<div class="cart">
  <div class="cart-title">
    <i class="material-icons" v-if="totalNumber && step===1" @click="$router.push('/')" title="Back to shop">arrow_back</i>
    <h1 class="title">Cart</h1>
    <div class="space" v-if="totalNumber && step===1"></div>
  </div>
  <empty v-if="!totalNumber"></empty>
  <stepone v-if="totalNumber && step===1"></stepone>
  <steptwo v-if="totalNumber && step===2"></steptwo>
  <finish v-if="totalNumber && step===3"></finish>
</div>
</template>

<script>
import Empty from './Empty'
import Stepone from './Stepone'
import Steptwo from './Steptwo'
import Finish from './Finish'
import { mapGetters } from 'vuex'
export default {
  name: 'cart',
  components: {
    Empty,
    Stepone,
    Steptwo,
    Finish
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

  .cart-title {
    width: 80%;
    display: flex;
    justify-content: center;

    i {
      font-size: 35px;
      margin-top: 5px;
      margin-right: auto;
    }

    .space {
      margin-left: auto;
    }
  }
}

.check-button {
  width: 80%;
  display: flex;
  justify-content: flex-end;
}
</style>
