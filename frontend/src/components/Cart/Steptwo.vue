<template>
<div class="steptwo">
  <shop-list></shop-list>
  <div class="summary">
    <h5>總金額 ${{totalAmount}}</h5>
  </div>
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
</style>
