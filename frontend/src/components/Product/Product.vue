<template>
  <div class="container">
    <div class="row">
      <div class="col-md-3">
        <div class="list-group sticky-top">
          <a href="#" v-for="cat in categories" :key="cat.id"
            class="list-group-item list-group-item-action"
            :class="{'active': activeCategories.id == cat.id}"
            @click="setActiveCategories(cat)">{{ cat.name }}</a>
        </div>
      </div>
      <div class="col-md-9">
        <div class="row">
          <product-card
            v-for="product in productList"
            :product="product"
            :key="product.id">
          </product-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProductCard from './ProductCard'
import { requestProduct } from '@/api/api'

export default {
  components: {
    ProductCard
  },
  data () {
    return {
      productList: []
    }
  },
  methods: {
    getProductList () {
      let params = { id: 1 }
      requestProduct.List(params).then(data => {
        console.log(data)
        this.productList = data
      })
    }
  },
  created () {
    this.getProductList()
  }
}
</script>

<style lang="scss">
</style>
