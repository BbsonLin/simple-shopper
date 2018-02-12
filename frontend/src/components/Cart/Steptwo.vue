<template>
<div class="steptwo">
  <shop-list></shop-list>
  <h5 class="amount">總金額 ${{totalAmount}}</h5>
</div>
</template>

<script>
import { mapGetters } from 'vuex'
import ShopList from './ShopList'
export default {
  name: 'steptwo',
  components: {
    ShopList
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
