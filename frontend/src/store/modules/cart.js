const state = {
  products: [],
  totalNumber: 0
}

const getters = {
  getCartProducts: (state) => {
    return state.products
  },
  getTotalNumber: (state) => {
    return state.totalNumber
  }
}

const actions = {
  updateCart ({ commit }, data) {
    commit('UPDATE_CART', data)
  },
  clearCart ({ commit }) {
    commit('CLEAR_CART')
  },
  removeProduct ({ commit }, id) {
    commit('REMOVE_PRODUCT', id)
  }
}

const mutations = {
  UPDATE_CART (state, data) {
    if (state.products.length) {
      let product = state.products.find(item => item.id === data.id)
      if (product) {
        product.number += data.number
      } else {
        state.products.push(data)
      }
    } else {
      state.products.push(data)
    }
    state.totalNumber += data.number
  },
  CLEAR_CART (state) {
    state.products = []
    state.totalNumber = 0
  },
  REMOVE_PRODUCT (state, id) {
    state.products = state.products.filter(item => item.id !== id)
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
