<template>
  <div class="col-sm-6 col-md-4 mb-3">
    <div class="card card-shadow border-0 text-center h-100">
      <img class="card-img-top" :src="product.image" :width="240" height="160" alt="Card image cap">
      <div class="card-body">
        <h5 class="card-title">{{ product.name }}</h5>
        <p class="card-text">{{ product.description }}</p>
        <p class="price">${{ product.price }}</p>
        <p class="stock">庫存：{{ product.stock }}</p>
      </div>
      <div class="input-group">
        <div class="input-group-prepend">
          <button class="btn btn-outline-secondary" type="button" @click="decrease"> - </button>
        </div>
        <input type="text" class="form-control text-center" v-model="number">
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" type="button" @click="increase"> + </button>
        </div>
      </div>
      <div class="card-footer border-0 text-center bg-white">
        <button class="btn btn-primary" @click="addToCart">加進購物車</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  props: {
    product: {
      type: Object
    }
  },
  data () {
    return {
      number: 1
    }
  },
  methods: {
    ...mapActions(['updateCart']),
    decrease () {
      if (this.number > 1) {
        this.number -= 1
      }
    },
    increase () {
      if (this.number < this.product.stock) {
        this.number += 1
      }
    },
    addToCart () {
      let product = {}
      product.id = this.product.id
      product.name = this.product.name
      product.price = this.product.price
      product.number = this.number
      product.subtotal = product.number * product.price
      this.updateCart(product)
    }
  }
}
</script>

<style lang="scss">
.card {
  overflow: hidden;

  &.card-shadow {
    box-shadow: 0 .25rem .5rem rgba(0, 0, 0, .1);
    transition: box-shadow .5s;
  }

  &:hover {
    &.card-shadow {
      box-shadow: 0 .25rem .5rem rgba(0, 0, 0, .3);
    }
  }

  .card-img-top:hover {
    transform: scale(1.2);
    transition: transform 1s;
  }

  .card-body {
    display: flex;
    flex-direction: column;

    .price {
      margin-top: auto;
    }

    .stock {
      margin: 0;
    }
  }
}

</style>
