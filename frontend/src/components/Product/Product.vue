<template>
  <div class="container">
    <div class="row">
      <div class="col-md-3">
        <div class="list-group sticky-top">
          <a href="#" v-for="category in categoryList" :key="category.id"
            class="list-group-item list-group-item-action"
            :class="{'active': activeCategory == category.id}"
            @click="setActiveCategory(category.id)">{{ category.name }}</a>
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
import { requestProduct, requestCategory } from '@/api/api'

export default {
  components: {
    ProductCard
  },
  data () {
    return {
      productList: [],
      categoryList: [],
      activeCategory: 1
    }
  },
  methods: {
    getProductList (categoryId) {
      let params = { id: categoryId }
      requestProduct.List(params).then(data => {
        this.productList = data
      }).catch(error => {
        console.log(error)
      })
    },
    getCategoryList () {
      requestCategory.List().then(data => {
        this.categoryList = data
      }).catch(error => {
        console.log(error)
      })
    },
    setActiveCategory (categoryId) {
      this.activeCategory = categoryId
      this.getProductList(categoryId)
    }
  },
  created () {
    this.getCategoryList()
    this.getProductList(1)
  }
}
</script>

<style lang="scss">
</style>
