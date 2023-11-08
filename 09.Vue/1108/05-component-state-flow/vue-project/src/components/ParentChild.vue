<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{  dynamicProps }}</p>
    <ParentGrandChild 
      :my-msg="myMsg"
      @update-name="updateName"
    />
    <button @click="$emit(`someEvent`)">클릭</button>
    <button @click="buttonClick">클릭</button>
    <button @click="emitArgs">추가 인자 전달</button>
  </div>
</template>

<script setup>
import ParentGrandChild from './ParentGrandChild.vue';

// defineProps(['myMsg'])
defineProps({
  myMsg: String, 
  dynamicProps : String
})

// emit 선언 방식
const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])

const buttonClick = function () {
  emit('someEvent')
}

const emitArgs = function () {
  emit('emitArgs', 1, 2, 3)
}

const updateName = function () {
  emit('updateName')
}
</script>

<style scoped>

</style>