exports.handler = function(event, context, callback) {
    var res = {
  "isBase64Encoded": true,
  "statusCode": 200,
  "headers": {
    "headerName": "headerValue"
  },
  "body": "..."
}
    
    callback(null, {"message": res});
}