<template>
  <vue-clip :options="options">
    <template slot="clip-uploader-action">
      <div class="uploader-action">
        <div class="dz-message"><h2> Click or Drag and Drop files here upload </h2></div>
      </div>
    </template>
  </vue-clip>
</template>

<script>
export default {
  data () {
    return {
      options: {
        url: '/upload',
        paramName: 'file',
        acceptedFiles: {
          extensions: ['image/*'],
          message: 'You are uploading an invalid file'
        }
      }
    }
  }
}
</script>