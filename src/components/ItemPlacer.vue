<template>
  <div>
    <vue-drag-resize v-for="item in collocation" :x="item.x" :y="item.y" :w="item.w" :h="item.h"
      :isActive="true" :parentLimitation="true">
      <img v-bind:src="item.image"></img>
    </vue-drag-resize>
  </div>
</template>

<script>
import VueDragResize from 'vue-drag-resize';

export default {
  props: [ 'collocation' ],
  components: {
    VueDragResize
  }
}
</script>
