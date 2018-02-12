<template>
<div class="steptwo">
  <div class="shop-list">
    <h4>商品列表</h4>
  </div>
  <table class="table">
    <tbody>
      <tr class="table-active">
        <td>商品名稱</td>
        <td>數量</td>
        <td>單價</td>
        <td>小計</td>
      </tr>
      <tr v-for="product in cartProducts">
        <td>{{ product.name }}</td>
        <td>{{ product.number }}</td>
        <td>{{ product.price }}</td>
        <td>{{ product.price * product.number }}</td>
      </tr>
    </tbody>
  </table>
  <!-- <div class="summary"> -->
  <!--   <h5>總金額 ${{totalAmount}}</h5> -->
  <!-- </div> -->
</div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'steptwo',
  data () {
    return {
    }
  },
  computed: {
    ...mapGetters({
      cartProducts: 'getCartProducts',
      totalNumber: 'getTotalNumber'
    })
  }
}
</script>

<style lang="scss">
</style>
