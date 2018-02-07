<template>
  <div class="jumbotron jumbotron-fluid jumbotron-bg d-flex align-items-end">
    <div class="container">
      <div class="bg-lighter p-3 text-black text-left">
        <h1 class="display-4">夏普夏普</h1>
        <p class="lead">This is a modified jumbotron</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss">
.jumbotron-bg {
  background-image: url('https://images.unsplash.com/photo-1483274816418-3975509c8f78');
  background-size: cover;
  background-position: center center;
  min-height: 10rem;
}

.bg-lighter {
  background-color: rgba(#fff, 0.45);
}
</style>
