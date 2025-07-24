import simplekml
kml = simplekml.Kml(open('./ptp_project_tmpl.kml').read())

# Example: Modifying a Placemark using simplekml
for f in kml.features:
    print(typeof(f))
#placemark.name = "Updated Name"
#placemark.description = "New description content."
#
# Example: Adding a new Placemark
#new_placemark = kml.newpoint(name="Another Point", coords=[(-122.083, 37.42)])
