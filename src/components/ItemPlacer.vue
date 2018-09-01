<template>
  <div>
    <vue-drag-resize v-for="(item, index) in collocation" :x="item.x" :y="item.y" :w="item.w" :h="item.h"
      :isActive="true" :parentLimitation="true" @resizestop="(rect) => onChange(index, rect)" @dragstop="(rect) => onChange(index, rect)">
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
  },
  methods: {
    onChange: function(index, rect) {
      this.$emit('change', index, rect)
    }
  }
}
</script>

<style scoped>
img {
  width: 100%;
  height: 100%;
}
</style>
