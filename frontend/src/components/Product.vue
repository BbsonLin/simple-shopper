<template>
  <div class="container">
    <div class="row">
      <div class="col-md-3">
        <div class="list-group">
          <a href="#" v-for="cat in categories" :key="cat.id"
            class="list-group-item list-group-item-action"
            :class="{'active': activeCategories.id == cat.id}"
            @click="setActiveCategories(cat)">{{ cat.name }}</a>
        </div>
      </div>
      <div class="col-md-9">
        <product-list></product-list>
      </div>
    </div>
  </div>
</template>

<script>
import ProductList from './ProductList'
import { mapGetters, mapActions } from 'vuex'

export default {
  components: {
    ProductList
  },
  computed: {
    ...mapGetters({
      activeCategories: 'getActiveCategories',
      categories: 'getCategories'
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
.card {
  &.card-shadow {
    box-shadow: 0 .25rem .5rem rgba(0, 0, 0, .1);
    transition: box-shadow .5s;
  }

  &:hover {
    &.card-shadow {
      box-shadow: 0 .25rem .5rem rgba(0, 0, 0, .3);
    }
  }
}
</style>
