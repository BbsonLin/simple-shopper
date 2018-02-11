<template>
<div class="stepone">
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
        <td>操作</td>
      </tr>
      <tr v-for="product in cartProducts">
        <td>{{ product.name }}</td>
        <td>{{ product.number }}</td>
        <td>{{ product.price }}</td>
        <td>{{ product.price * product.number }}</td>
        <td><i class="material-icons">clear</i></td>
      </tr>
    </tbody>
  </table>
  <div class="total">
    <span>總金額 $</span>
  </div>
</div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'stepone',
  computed: {
    ...mapGetters({
      cartProducts: 'getCartProducts',
      totalNumber: 'getTotalNumber'
    })
  }
}
</script>

<style lang="scss">
.stepone {
  width: 80%;

  .shop-list {
    display: flex;
    justify-content: flex-start;
  }
}
</style>
