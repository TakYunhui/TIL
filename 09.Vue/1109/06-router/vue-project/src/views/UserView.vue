<template>
  <div>
    <h1>UserView</h1>
    <h2>{{ $route.params.id }}번 유저의 페이지입니다.</h2>
    <h2>{{ userId }}번 유저의 페이지입니다.</h2>
    <button @click="goHome">홈으로!</button>
    <button @click="goAnotherUser">100 st user</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'
const route = useRoute()
const userId = ref(route.params.id)

// 프로그래밍 방식 네비게이션
const router = useRouter()
const goHome = function () {
  // router.push({ name: 'home'})
  router.replace({name: 'home'})
}

// In-component Guard
onBeforeRouteLeave((to, form) => {
  const answer = window.confirm('정말 떠나냐?')
  if (answer === false) {
    return false
  }
})

const goAnotherUser = function () {
  router.push({name: 'user', params:{id:100}})
}

onBeforeRouteUpdate((to, from) => {
  userId.value = to.params.id
})
</script>

<style scoped>

</style>