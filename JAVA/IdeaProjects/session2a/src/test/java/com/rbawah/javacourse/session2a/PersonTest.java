package com.rbawah.javacourse.session2a;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class PersonTest {
    @Test
    public void shouldReturnHelloWorld() {
        Person myself = new Person();
        assertEquals("Hello, World!", myself.helloWorld());

    }
}
