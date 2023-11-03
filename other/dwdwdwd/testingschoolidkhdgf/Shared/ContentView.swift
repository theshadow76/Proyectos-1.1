//
//  ContentView.swift
//  Shared
//
//  Created by Vigo Walker on 09-06-22.
//

import SwiftUI

struct ContentView: View {
    @Binding var document: testingschoolidkhdgfDocument

    var body: some View {
        TextEditor(text: $document.text)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView(document: .constant(testingschoolidkhdgfDocument()))
    }
}
