<template>
  <div>
    <vue-drag-resize class="img-box" v-for="(item, index) in collocation.layers" :key="item.picUrl" :x="item.x/2" :y="item.y/2" :w="item.width/2" :h="item.height/2" :isActive="item.dynamic" :isDraggable="item.dynamic" :isResizable="item.dynamic" @resizestop="(rect) => onChange(index, rect)" @dragstop="(rect) => onChange(index, rect)">
      <img :style="'transform: rotate('  + item.rotate + 'deg);'" v-bind:src="item.picUrl"/>
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
  max-width: 100%;
  max-height: 100%;
  width: auto;
  height: auto;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
}
</style>
