var WebpackBeforeBuildPlugin = require('before-build-webpack');
const path = require('path');
const fs = require('fs');



export default (config, env, helpers) => {
  // build destination
  let p = path.resolve('../static');
  const before_build = new WebpackBeforeBuildPlugin(function(stats, callback) {
    // Clears output folder from all previous things except folders
    fs.readdirSync(p).forEach(filename => {
      const filenamePath = path.join(p, filename);
      if (!fs.lstatSync(filenamePath).isDirectory()) {
        fs.unlinkSync(filenamePath);
      }
    });
    callback();
  });
  config.plugins.push(before_build);

  // move index.html into template folder
  let html_plugin = helpers.getPluginsByName(config, 'HtmlWebpackPlugin').pop();
  html_plugin.plugin.options.filename = path.resolve('../templates/index.html');
  // overwrite config to serve files from static folder
  Object.assign(config.output, {
    path: p,
    publicPath: '/static/'
  });
  console.log(config.output);
};