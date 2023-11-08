<template>
  <h1>App.vue</h1>
  <MyComponents />
</template>

<script setup>
// import MyComponents from './components/MyComponents.vue';
// @ -> src -> 절대경로 잡기: 상대경로로 매번 찾기 어렵기 때문
import MyComponents from '@/components/MyComponents.vue';
</script>

<style scoped>

</style>