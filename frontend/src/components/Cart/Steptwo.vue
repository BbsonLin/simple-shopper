<template>
<div class="steptwo">
  <shop-list></shop-list>
  <h5 class="amount">總金額 ${{totalAmount}}</h5>
  <check></check>
</div>
</template>

<script>
import { mapGetters } from 'vuex'
import ShopList from './ShopList'
import Check from './Check'
export default {
  name: 'steptwo',
  components: {
    ShopList,
    Check
  },
  computed: {
    ...mapGetters({
      totalAmount: 'getTotalAmount'
    })
  }
}
</script>

<style lang="scss">
.steptwo {
  width: 80%;

  .amount {
    text-align: right;
  }
}
</style>
