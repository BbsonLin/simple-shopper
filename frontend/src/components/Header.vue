<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">SimpleShopper</a>
    <div class="dropdown ml-auto" ref="dropdown">
      <button class="btn btn-sm btn-cart" @click="toggleMenu()">
        <span class="h6">購物車</span>
        <i class="fa fa-shopping-cart fa-2x"></i>
        <span class="badge badge-pill badge-danger">{{ totalNumber }}</span>
      </button>
      <div class="shopper-menu" :class="{ 'open': menuOpen }">
        <h6>已選擇商品
          <button class="btn btn-link" @click="clearCart">清空</button>
        </h6>
        <table class="table">
          <tbody>
            <tr v-for="item in items" :key="item.id">
              <td><i class="material-icons" @click="removeCartProduct(item)">clear</i></td>
              <td>{{ item.name }}</td>
              <td>{{ item.number }} 件</td>
              <td>${{ item.price * item.number }}</td>
            </tr>
          </tbody>
        </table>
        <a href="javascript:void(0)" class="btn btn-primary btn-block" @click="$router.push('/cart')">結帳去</a>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  data () {
    return {
      menuOpen: false
    }
  },
  computed: {
    ...mapGetters({
      items: 'getCartProducts',
      totalNumber: 'getTotalNumber'
    })
  },
  methods: {
    ...mapActions(['clearCart', 'removeProduct']),
    toggleMenu () {
      this.menuOpen = !this.menuOpen
    },
    documentClick (e) {
      // Handle closing dropdown when clicking outside of it
      let el = this.$refs.dropdown
      let target = e.target
      if (el === undefined) {
        return 0
      } else if ((el !== target) && !el.contains(target)) {
        this.menuOpen = false
      }
    },
    removeCartProduct (product) {
      this.removeProduct(product)
    }
  },
  created () {
    document.addEventListener('click', this.documentClick)
  }
}
</script>

<style lang="scss">
.dropdown {
  .btn-cart {
    position: fixed;
    z-index: 10;
    background-color: rgba(255, 255, 255, .5);
    top: .5rem;
    right: .5rem;

    &:focus {
      box-shadow: 0 0 0 #fff;
    }

    .badge {
      position: absolute;
      top: -0.25rem;
      right: -0.25rem;
    }
  }
}

.shopper-menu {
  display: none;
  position: fixed;
  background-color: #fff;
  list-style: none;
  border: 1px solid #ccc;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
  border-radius: 4px;
  right: 0;
  min-width: 300px;
  z-index: 10;
  padding: 1rem;

  &.open {
    display: block;
  }
}

.material-icons {
  cursor: pointer;
}
</style>
