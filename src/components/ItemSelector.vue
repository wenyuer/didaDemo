<template>
  <div>
    <el-row id="item-row">
      <el-col class="item-col" :span="4" v-for="item in items">
        <el-card>
          <div class="image-wrapper">
            <img v-bind:src="item.image"></img>
          </div>
          <el-button type="text" v-on:click="selectItem(item.id)"> 继续搭配 </el-button>
        </el-card>
      </el-col>
    </el-row>
    <div>
      <el-select v-model="type">
        <el-option value="0" label="上衣"></el-option>
        <el-option value="1" label="下衣"></el-option>
        <el-option value="2" label="裙装"></el-option>
        <el-option value="3" label="女鞋"></el-option>
        <el-option value="4" label="箱包"></el-option>
        <el-option value="5" label="饰品"></el-option>
      </el-select>
      <el-button id="refresh" type="primary" icon="el-icon-refresh" v-on:click="reload()"> 换一批 </el-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [],
      type: "0"
    }
  },
  methods: {
    reload: function() {
      this.$http.get('http://localhost:5000/items?type=' + this.type).then((response) => {
        this.items = response.data
      })
    },
    selectItem: function(id) {
      this.$http.get('http://localhost:5000/collocation?itemId=' + id).then((response) => {
        this.$emit('collocation', response.data)
      })
    }
  },
  mounted: function() {
    this.reload()
  }
}
</script>

<style scoped>
#item-row {
  margin-bottom: 10px;
}
.el-col:nth-child(n+2) .el-card {
  margin-left: 10px;
}
.el-card .image-wrapper {
  height: 150px;
  line-height: 150px;
}
.el-card img {
  margin: auto;
  display: block;
  width: auto;
  height: auto;
  max-width: 100%;
  max-height: 150px;
}
#refresh {
  margin-left: 10px;
}
</style>
