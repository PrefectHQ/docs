export default (request: Request): Response => {
  if (request.method !== 'POST') {
    return new Response(null, {
      status: 400,
    })
  }

  // Discard analytics events from the legacy docs site.
  return new Response(null, {
    status: 204,
  })
}
