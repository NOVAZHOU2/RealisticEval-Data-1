package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

public class Tester {

    @Test
    public void testGetPriceWithinDefaultRange() {
        double price = RecipePrice.getPrice("recipe123");
        assertTrue(price >= 10);
        assertTrue(price <= 30);
    }

    @Test
    public void testGetPriceSameRecipeId() {
        double price1 = RecipePrice.getPrice("recipe123");
        double price2 = RecipePrice.getPrice("recipe123");
        assertEquals(price1, price2, 0.01);
    }

    @Test
    public void testGetPriceDifferentRecipeIds() {
        double price1 = RecipePrice.getPrice("recipe123");
        double price2 = RecipePrice.getPrice("recipe456");
        assertNotEquals(price1, price2, 0.01);
    }

    @Test
    public void testGetPriceWithinCustomRange() {
        double minVal = 20;
        double maxVal = 50;
        double price = RecipePrice.getPrice("recipe789", minVal, maxVal);
        assertTrue(price >= minVal);
        assertTrue(price <= maxVal);
    }

    @Test
    public void testGetPriceLongRecipeId() {
        String longRecipeId = "recipe" + "A".repeat(1000);
        double price = RecipePrice.getPrice(longRecipeId);
        assertTrue(price >= 10);
        assertTrue(price <= 30);
    }
}