<template>
  <div>
    <vue-drag-resize v-for="item in items" :x="item.x" :y="item.y" :w="item.w" :h="item.h"
      :isActive="true" :isResizable="false" :parentLimitation="true">{{ item }}</vue-drag-resize>
  </div>
</template>

<script>
import VueDragResize from 'vue-drag-resize';

export default {
  components: {
    VueDragResize
  },
  data() {
    return {
      items: []
    }
  },
  methods: {
    reload: function() {
      this.items = [
        {
          url: 'a',
          x: 0,
          y: 0,
          w: 100,
          h: 100
        },
        {
          url: 'b',
          x: 0,
          y: 100,
          w: 100,
          h: 100
        },
        {
          url: 'c',
          x: 120,
          y: 50,
          w: 50,
          h: 50
        }
      ]
    }
  },
  mounted: function() {
    this.reload()
  }
}
</script>

<style>
</style>
