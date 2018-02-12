const state = {
  products: [],
  totalNumber: 0,
  step: 1
}

const getters = {
  getCartProducts: (state) => {
    return state.products
  },
  getTotalNumber: (state) => {
    return state.totalNumber
  },
  getStep: (state) => {
    return state.step
  }
}

const actions = {
  updateCart ({ commit }, data) {
    commit('UPDATE_CART', data)
  },
  clearCart ({ commit }) {
    commit('CLEAR_CART')
  },
  removeProduct ({ commit }, product) {
    commit('REMOVE_PRODUCT', product)
  },
  addStep ({ commit }) {
    commit('ADD_STEP')
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
    state.step = 1
  },
  REMOVE_PRODUCT (state, product) {
    state.products = state.products.filter(item => item.id !== product.id)
    state.totalNumber -= product.number
  },
  ADD_STEP (state) {
    state.step++
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
