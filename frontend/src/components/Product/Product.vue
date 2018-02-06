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
          <product-card v-for="product in products"
                        :product="product"
                        :key="product.id"></product-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProductCard from './ProductCard'
import { mapGetters, mapActions } from 'vuex'

export default {
  components: {
    ProductCard
  },
  computed: {
    ...mapGetters({
      activeCategories: 'getActiveCategories',
      categories: 'getCategories',
      products: 'getProducts'
    })
  },
  methods: {
    ...mapActions(['setActiveCategories'])
  },
  created () {
    this.setActiveCategories(this.categories[0])
  }
}
</script>

<style lang="scss">
</style>
