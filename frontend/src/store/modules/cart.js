const state = {
  products: [],
  totalNumber: 0,
  totalAmount: 0,
  check: {
    method: {},
    store: {}
  },
  step: 1
}

const getters = {
  getCartProducts: (state) => {
    return state.products
  },
  getTotalNumber: (state) => {
    return state.totalNumber
  },
  getTotalAmount: (state) => {
    return state.totalAmount
  },
  getStep: (state) => {
    return state.step
  },
  getCheck: (state) => {
    return state.check
  }
}

const actions = {
  updateCart ({ commit }, data) {
    commit('UPDATE_CART', data)
    commit('CALTOTALAMOUNT')
  },
  clearCart ({ commit }) {
    commit('CLEAR_CART')
  },
  removeProduct ({ commit }, product) {
    commit('REMOVE_PRODUCT', product)
    commit('CALTOTALAMOUNT')
  },
  addStep ({ commit }) {
    commit('ADD_STEP')
  },
  updateCheck ({ commit }, data) {
    commit('UPDATE_CHECK', data)
  }
}

const mutations = {
  UPDATE_CART (state, data) {
    if (state.products.length) {
      let product = state.products.find(item => item.id === data.id)
      if (product) {
        product.subtotal = product.number * product.price
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
    state.totalAmout = 0
    state.step = 1
  },
  REMOVE_PRODUCT (state, product) {
    state.products = state.products.filter(item => item.id !== product.id)
    state.totalNumber -= product.number
  },
  ADD_STEP (state) {
    state.step++
  },
  CALTOTALAMOUNT (state) {
    let totalAmount = 0
    state.products.forEach(product => {
      totalAmount += (product.number * product.price)
    })
    state.totalAmount = totalAmount
  },
  UPDATE_CHECK (state, data) {
    state.check.method = data.method
    state.check.store = data.store
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
