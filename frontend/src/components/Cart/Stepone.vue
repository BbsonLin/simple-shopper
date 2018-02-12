<template>
<div class="stepone">
  <shop-list></shop-list>
  <div class="summary">
    <h5>總金額 ${{totalAmount}}</h5>
    <button class="btn btn-primary" @click="addStep">結帳</button>
  </div>
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import ShopList from './ShopList'
export default {
  name: 'stepone',
  components: {
    ShopList
  },
  computed: {
    ...mapGetters({
      totalAmount: 'getTotalAmount'
    })
  },
  methods: {
    ...mapActions(['addStep'])
  }
}
</script>

<style lang="scss">
.stepone {
  width: 80%;

  .summary {
    display: flex;
    justify-content: flex-end;

    h5 {
      margin: auto 5px auto 0;
    }
  }
}
</style>
