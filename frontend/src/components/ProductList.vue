<template>
  <div class="row">
    <div class="col-sm-6 col-md-4 mb-3" v-for="product in products" :key="product.id">
      <div class="card card-shadow border-0 text-center h-100">
        <img class="card-img-top" :src="product.image" alt="Card image cap">
        <div class="card-body">
          <h5 class="card-title">{{ product.name }}</h5>
          <p class="card-text">{{ product.description }}</p>
        </div>
        <div class="card-footer border-0 text-center bg-white">
          <button class="btn btn-primary">加進購物車</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters({
      products: 'getProducts'
    })
  }
}
</script>

<style lang="scss">
</style>
