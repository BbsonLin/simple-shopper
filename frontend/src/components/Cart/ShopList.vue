<template>
<div class="shop-list">
  <div class="list-title">
    <h4>商品列表</h4>
  </div>
  <table class="table">
    <tbody>
      <tr class="table-active">
        <td>商品名稱</td>
        <td>數量</td>
        <td>單價</td>
        <td>小計</td>
        <td v-if="step===1">操作</td>
      </tr>
      <tr v-for="product in cartProducts">
        <td>{{ product.name }}</td>
        <td>{{ product.number }}</td>
        <td>{{ product.price }}</td>
        <td>{{ product.price * product.number }}</td>
        <td v-if="step===1"><i class="material-icons">clear</i></td>
      </tr>
    </tbody>
  </table>
</div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'shop-list',
  computed: {
    ...mapGetters({
      cartProducts: 'getCartProducts',
      totalNumber: 'getTotalNumber',
      step: 'getStep'
    })
  }
}
</script>

<style lang="scss">
.shop-list {
  .list-title {
    display: flex;
    justify-content: flex-start;
  }
}
</style>
